from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, TabPane, Markdown


class Pinecone(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with TabbedContent(initial="stats"):
            with TabPane("Statistics", id="stats"):
                yield Markdown("Statistics")
            with TabPane("Customization", id="customiztion"):
                yield Markdown("Customization")
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark