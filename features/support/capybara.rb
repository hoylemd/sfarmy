require 'minitest/reporters'
require 'capybara/cucumber'
require 'capybara/poltergeist'
require 'byebug'
require 'HTTParty'
require 'json'

Capybara.javascript_driver = :poltergeist
Capybara.default_driver = :poltergeist
Capybara.app_host = ENV['BASE_URL']

# load the cache
Before do |scenario|
  cache_path = ENV['CACHE_PATH'] || 'features/cache.json'
  if File.exist?(cache_path)
    @cache = JSON.parse(File.open(cache_path, 'r').read)
  else
    @cache = {}
  end
end

# save screenshots on failure
After do |scenario|
  if scenario.failed?
    path = "screenshots/debug_#{Time.now.to_i}.png"
    page.save_screenshot(path)
    embed path, 'image/png', 'SCREENSHOT'
  end
end

# save the cache
After do |scenario|
  cache_path = ENV['CACHE_PATH'] || 'features/cache.json'

  File.open(cache_path, 'w').puts @cache.to_json
end
