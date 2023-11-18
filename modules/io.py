from cutepy import RGB
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML


def _generate_oscillating_gradient(start_color, end_color, steps):
    """
    Generates an oscillating gradient between two colors over a specified number of steps.

    :param start_color: A tuple representing the RGB values of the start color.
    :param end_color: A tuple representing the RGB values of the end color.
    :param steps: The number of steps in the gradient.
    :return: A list of RGB color tuples representing the gradient.
    """

    gradient = []
    half_steps = steps // 2

    for i in range(half_steps):
        gradient_color = [
            int(start_color[j] + (end_color[j] - start_color[j]) * (i / half_steps))
            for j in range(3)
        ]
        gradient.append(gradient_color)

    for i in range(half_steps, steps):
        gradient_color = [
            int(
                end_color[j]
                + (start_color[j] - end_color[j]) * ((i - half_steps) / half_steps)
            )
            for j in range(3)
        ]
        gradient.append(gradient_color)

    return gradient


def _print_oscillating_gradient(message, start_color, end_color, newline=True):
    """
    Prints a message with each character colored according to an oscillating gradient between two colors.

    :param message: The message to be printed.
    :param start_color: A tuple representing the RGB values of the start color.
    :param end_color: A tuple representing the RGB values of the end color.
    :param newline: Boolean indicating whether to add a newline at the end of the message.
    """

    gradient = _generate_oscillating_gradient(start_color, end_color, len(message))
    reset_code = RGB.reset

    for i, char in enumerate(message):
        color_code = RGB.print(*gradient[i])
        print(f"{color_code}{char}", end="")

    print(f"{reset_code}", end="" if not newline else "\n")


def hex_to_rgb(hex_color):
    """
    Converts a hex color string to an RGB color tuple.

    :param hex_color: A string representing the color in hex format.
    :return: A tuple representing the color in RGB format.
    """

    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def input_data(exploit_name, prompt_title):
    """
    Prompts the user for input using a custom prompt style.

    :param exploit_name: The name of the exploit module.
    :param prompt_title: The title of the prompt.
    :return: The user's input as a string.
    """

    color_hex = "e3d5ae"
    color_rgb = hex_to_rgb(color_hex)
    session = PromptSession()

    color_hex_for_prompt = "#{:02x}{:02x}{:02x}".format(*color_rgb)

    style = Style.from_dict(
        {
            "input_prompt": f"fg:{color_hex_for_prompt}",
        }
    )

    full_prompt = HTML(
        f"<input_prompt>axer({exploit_name}) ~ {prompt_title} ➜ </input_prompt>"
    )

    user_input = session.prompt(full_prompt, style=style).strip()
    return user_input


def print_success(message):
    """
    Prints a success message in an oscillating gradient of green colors.

    :param message: The success message to be printed.
    """

    start_color = (0, 255, 0)
    end_color = (144, 238, 144)
    _print_oscillating_gradient("[SUCCESS] " + message, start_color, end_color)


def print_error(message):
    """
    Prints an error message in an oscillating gradient of red colors.

    :param message: The error message to be printed.
    """

    start_color = (255, 0, 0)
    end_color = (255, 99, 71)
    _print_oscillating_gradient("[ERROR] " + message, start_color, end_color)


def print_status(message):
    """
    Prints a status message in an oscillating gradient of blue colors.

    :param message: The status message to be printed.
    """

    start_color = (30, 144, 255)
    end_color = (135, 206, 250)
    _print_oscillating_gradient("[STATUS] " + message, start_color, end_color)


def print_info(message):
    """
    Prints an informational message in an oscillating gradient of yellow colors.

    :param message: The informational message to be printed.
    """

    start_color = (255, 255, 0)
    end_color = (255, 255, 224)
    _print_oscillating_gradient("[INFO] " + message, start_color, end_color)


if __name__ == "__main__":
    """
    Main execution block for testing the functions in the script.
    It demonstrates the usage of print functions and the input_data function.
    """

    print_success("The operation was completed successfully!")
    print_error("An error occurred during the operation.")
    print_info("This is an informational message.")
    print_status("The process is underway...")
    input_data("ExploitName", "Your input")
