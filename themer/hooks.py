app_name = "themer"
app_title = "Themer"
app_publisher = "unganisha networks"
app_description = "themer for unganisha"
app_email = "nwachira@unganishanetworks.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#app_include_css = "/assets/themer/css/themer.css"
#app_include_js =  "/assets/themer/css/style.css",
#app_include_js = "/assets/themer/css/bootstrap.min.css",
#app_include_js = "/assets/themer/lib/owlcarousel/assets/owl.carousel.min.css",
#app_include_js = "/assets/themer/lib/lightbox/css/lightbox.min.css",
#app_include_js = "/assets/themer/js/main.js",
#app_include_js= "/assets/themer/lib/easing/easing.min.js",
#app_include_js = "/assets/themer/lib/waypoints/waypoints.min.js",
#app_include_js= "/assets/themer/lib/lightbox/js/lightbox.min.js",
#app_include_js= "/assets/themer/lib/owlcarousel/owl.carousel.min.js"


# include js, css files in header of web template
#eb_include_css = "/assets/themer/css/style.css",

#web_include_js = "/assets/themer/js/main.js",


# include custom scss in every website theme (without file extension ".scss")
#website_theme_scss = "themer/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "themer/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "themer.utils.jinja_methods",
# 	"filters": "themer.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "themer.install.before_install"
# after_install = "themer.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "themer.uninstall.before_uninstall"
# after_uninstall = "themer.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "themer.utils.before_app_install"
# after_app_install = "themer.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "themer.utils.before_app_uninstall"
# after_app_uninstall = "themer.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "themer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"themer.tasks.all"
# 	],
# 	"daily": [
# 		"themer.tasks.daily"
# 	],
# 	"hourly": [
# 		"themer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"themer.tasks.weekly"
# 	],
# 	"monthly": [
# 		"themer.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "themer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "themer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "themer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["themer.utils.before_request"]
# after_request = ["themer.utils.after_request"]

# Job Events
# ----------
# before_job = ["themer.utils.before_job"]
# after_job = ["themer.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"themer.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

