# rubocop:disable Style/MethodLength
def page_mappings
  # TODO: replace these with actual mappings
  @page_mappings ||= {
    'signup' => '/signup',
    'home' => '/',
    'login' => '/login',
    'logout' => '/logout',
    'user profile' => %r{/users/[0-9]+$} # regex example
  }
end
# rubocop:enable Style/MethodLength

def page_known?(page_name)
  page_mappings.key?(page_name)
end

def assert_page_known(page_name)
  assert page_known?(page_name),
         "the specified page '#{page_name}' is not known to the test suite"
end

def assert_at_page(page_name)
  assert_page_known page_name
  path = page_mappings[page_name]
  assert path.match(current_path), "Expected to be at #{path}, " \
                                   "but was actually at #{current_path}"
end

def visit_page(page_name)
  assert_page_known page_name
  visit page_mappings[page_name]
end

Given(/I am on the (.*) page$/) do |page_name|
  visit_page(page_name)
end

When(/I visit the (.*) page$/) do |page_name|
  visit_page(page_name)
end

When(/I hover over "(.*)"$/) do |text|
  find('.js-hoverable', text: text).hover
end

When(/I click "(.*)"$/) do |text|
  click_on text
end

When(/I click the "(.*)" button$/) do |label|
  click_button label
end

def should_see(text, negate = false)
  if negate
    assert_no_text text
  else
    assert_text text
  end
end

Then(/I should( not)? see "(.*)"$/) do |negate, text|
  should_see text, negate
end

Then(/I should( not)? see the following phrases:$/) do |negate, phrases|
  phrases.raw.each do |phrase|
    should_see phrase.first, negate
  end
end

Then(/I should see a "(.+)" field$/) do |field_name|
  label = page.find('label', text: field_name)
  assert_selector "input##{label[:for]}"
end

Then(/I should see a "(.*)" button$/) do |label|
  assert has_button?(label), "No '#{label}' button found."
end

# options
#  type: String for the type of alert to look for.
#         Will select any flash if omitted
#         currently used: 'success' and 'danger'
#  Remaining options will be passed to assert_selector.
#    The following ones are especially useful:
#  text: String or regexp for the content of the message
#  count/minimum/maximum: bounds on the number of matches
#  TODO: this is built for rails flashes, but could be modified to work anywhere
def assert_flash(options)
  locator = '.alert'
  locator += ".alert-#{options.delete(:type)}" if options[:type]

  assert_selector locator, options
end

Then(/I should( not)? see a([a-z ]+) flash$/) do |negate, type_string|
  options = { type: type_string == 'n error' ? 'danger' : type_string.strip }
  options[:count] = 0 if negate
  assert_flash options
end

Then(/I should see a ([a-z]+) flash that says "(.*)"$/) do |type, message|
  assert_flash type: type, text: message
end

Then(/I should not see any validation errors$/) do
  assert_selector('#error_explanation', count: 0)
end

def assert_validation_error(text, negate = false)
  options = { text: text }
  options[:count] = 0 if negate
  assert_selector('#error_explanation li', options)
end

Then(/I should( not)? see a validation error that says "(.*)"$/) do |neg, text|
  assert_validation_error text, neg
end

Then(/I should( not)? see the following validation errors:$/) do |neg, errors|
  errors.raw.each do |row|
    assert_validation_error row.first, neg
  end
end

When(/I enter "(.+)" into "(.+)"$/) do |text, label|
  fill_in label, with: text
end

When(/I enter gibberish into "(.+)"$/) do |label|
  fill_in label, with: random_string
end
