# TODO: Sessions in Flask
# A session is the time between a user logging in and logging out of a server. Session data is stored on the server in a temporary folder, and each user is assigned a unique session ID.

# Session ID
# The Session object is a dictionary that contains the key-value pair of the variables associated with the session. A SECRET_KEY is used to store the encrypted data on the cookies.

# Example:

# Session[key] = value   // stores the session value
# Session.pop(key, None)  // releases a session variable