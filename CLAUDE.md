# Development Guide for sphinx-new-tab-link

## Build & Test Commands
- Format code: `task format`
- Run tests: `task test` (includes pre/post hooks for format and check)
- Lint & type check: `task check`
- Run single test: `pytest tests/test_file.py::test_function -v`
- Complete workflow: `task format && task test && task check`

## Environment Setup
- Project uses Python virtual environment (venv directory)
- Claude Code and other AI tools should ignore the venv directory
- Use Python 3.9 or higher for development

## Code Style Guidelines
- Line length: 79 characters
- Formatting: Black with black profile for isort
- Type annotations required, use `typing.TYPE_CHECKING` for annotation imports
- Import order: stdlib → third-party → local modules (enforced by isort)
- Naming: lowercase_with_underscores for variables, functions, methods

## Error Handling
- Use specific exceptions with clear error messages
- Test expected exceptions explicitly

## Development Workflow
- Write tests before implementation
- Ensure all tests pass before committing
- CI runs tests on Python 3.9-3.13
