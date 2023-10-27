from typing import List, Dict


class Session:
    """Session object."""

    def __init__(
        self,
        # Id of the session
        id: str,
    ):
        self.id = id
        self.messages_history: List[str] = []
        sessions_id[id] = self

    def delete(self):
        """Delete the session."""
        sessions_id.pop(self.id, None)


sessions_id: Dict[str, Session] = {}
