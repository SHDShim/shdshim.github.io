#!/usr/bin/env ruby
# frozen_string_literal: true

require "optparse"
require "yaml"

options = {}

parser = OptionParser.new do |opts|
  opts.banner = "Usage: ruby scripts/add_research_news.rb --date YYYY.MM --text TEXT --source-label LABEL --source-url URL"

  opts.on("--date DATE", "Date in YYYY.MM format") { |v| options[:date] = v }
  opts.on("--text TEXT", "News text") { |v| options[:text] = v }
  opts.on("--source-label LABEL", "Source label") { |v| options[:source_label] = v }
  opts.on("--source-url URL", "Source URL") { |v| options[:source_url] = v }
end

parser.parse!

required = %i[date text source_label source_url]
missing = required.select { |k| options[k].to_s.strip.empty? }
unless missing.empty?
  warn "Missing required options: #{missing.join(', ')}"
  warn parser.banner
  exit 1
end

unless options[:date].match?(/^\d{4}\.\d{2}$/)
  warn "Invalid --date format. Use YYYY.MM (example: 2026.04)."
  exit 1
end

file = "_data/research.yml"
data = YAML.load_file(file)
data["news"] ||= {}

latest = data["news"]["latest"]
latest = [latest] if latest.is_a?(Hash)
latest ||= []

earlier = data["news"]["earlier"] || []

new_item = {
  "date" => options[:date],
  "text" => options[:text],
  "source_label" => options[:source_label],
  "source_url" => options[:source_url]
}

# Remove duplicates by source URL across latest.
latest.reject! { |item| item["source_url"] == new_item["source_url"] }

# Add newest item first.
latest.unshift(new_item)

# Move older latest entries to earlier archive after keeping top two.
overflow = latest[2..] || []
latest = latest.first(2)

overflow.each do |item|
  next if item["source_url"].to_s.empty?

  earlier_entry = {
    "year" => item["date"].to_s[0, 4],
    "text" => item["text"],
    "links" => [
      {
        "label" => item["source_label"],
        "url" => item["source_url"]
      }
    ]
  }

  # Remove existing duplicates in earlier by URL before prepend.
  earlier.reject! do |entry|
    links = entry["links"] || []
    links.any? { |link| link["url"] == item["source_url"] }
  end
  earlier.unshift(earlier_entry)
end

# Ensure no duplicate URLs remain in earlier.
seen = {}
earlier = earlier.reject do |entry|
  links = entry["links"] || []
  urls = links.map { |link| link["url"] }.compact
  dedupe = urls.any? { |u| seen[u] }
  urls.each { |u| seen[u] = true }
  dedupe
end

data["news"]["latest"] = latest
data["news"]["earlier"] = earlier

File.write(file, data.to_yaml(line_width: -1))
puts "Updated #{file}: latest=#{latest.length}, earlier=#{earlier.length}"
