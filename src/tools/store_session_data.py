from typing import Any, Dict
from google.adk.tools import ToolContext

USER_NAME_SCOPE_LEVELS = ("temp", "user", "app")


# Write to session state using tool_context
# The 'user:' prefix indicates this is user-specific data.
def save_userinfo(
    tool_context: ToolContext, cv_path: str, location: str
) -> Dict[str, Any]:
    """
    Tool to record and save cv path and location in session state.

    Args:
        cv_path: The cv path to store in session state
        location: The name of the user's desired location
    """
    # Write to session state using the 'user:' prefix for user data
    tool_context.state["user:path"] = cv_path
    tool_context.state["user:location"] = location

    return {"status": "success"}


# Read from session state
def retrieve_userinfo(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Tool to retrieve cv_path and location from session state.
    """
    cv_path = tool_context.state.get("user:path", "Path not found")
    location = tool_context.state.get("user:location", "Location not found")

    return {"status": "success", "cv_path": cv_path, "location": location}
