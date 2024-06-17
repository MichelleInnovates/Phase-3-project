import click

def print_error(message):
    """
    Print an error message in red color.
    """
    click.secho(message, fg='red')

def print_success(message):
    """
    Print a success message in green color.
    """
    click.secho(message, fg='green')

def print_warning(message):
    """
    Print a warning message in yellow color.
    """
    click.secho(message, fg='yellow')

def prompt_choice(options):
    """
    Prompt the user to select an option from a list of choices.
    """
    choice = None
    while choice not in options:
        choice = click.prompt(f"Select an option ({', '.join(options)})")
    return choice

def confirm_action(message):
    """
    Prompt the user to confirm an action.
    """
    return click.confirm(message)