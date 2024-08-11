# Write a function to filter and sort a list of restaurants based on their ratings. Each restaurant should be represented as a dictionary containing keys for 'name' and 'rating'. The function should allow the user to specify a minimum rating threshold. If no threshold is specified, the default should be set to 4.0. The function should return a list of restaurant names that meet or exceed the rating threshold, sorted alphabetically.
#
# Functionality:
#
# Input Handling: Prompt the user to enter the number of restaurants they wish to input. For each restaurant, the user should provide a name and a numerical rating.
#
# Rating Filter: By default, only include restaurants with a rating of 4.0 or higher unless the user specifies a different minimum.
#
# Sorting: The output list should be alphabetically sorted by the restaurant name for those that meet the rating criteria.
#
# User Feedback: Display the filtered and sorted list of restaurant names to the user.
#
#
# Enter number of restaurants: 3
# Enter restaurant name: Joe's Grill
# Enter restaurant rating: 4.5
# Enter restaurant name: Pizza Paradise
# Enter restaurant rating: 3.8
# Enter restaurant name: The Gourmet Salad
# Enter restaurant rating: 4.8
# Restaurants with a rating above 4.0: ['The Gourmet Salad', 'Joe's Grill']