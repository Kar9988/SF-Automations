import os
import platform
import click
from contants.main_constant import UBUNTU_WINDOWS_BASE_COMMAND, BASE_TEST_COMMAND
from page.sf_login_page import LoginPage
from page.sf_base_page import SfBasePage


@click.command()
@click.option(
    "-m",
    "--marker",
    required=False,
    default="",
    type=str,
    help="The marker of pytest. Should be added smoke or regression"
)
def main(marker: str):
    if platform.system() != "Windows":
        if len(marker) > 0:
            os.system(f"{UBUNTU_WINDOWS_BASE_COMMAND} {BASE_TEST_COMMAND} -m {marker}")
        else:
            os.system(f"{UBUNTU_WINDOWS_BASE_COMMAND} {BASE_TEST_COMMAND}")
    else:
        if marker:
            os.system(f"{UBUNTU_WINDOWS_BASE_COMMAND} {BASE_TEST_COMMAND} -m {marker}")
        else:
            os.system(f"{UBUNTU_WINDOWS_BASE_COMMAND} {BASE_TEST_COMMAND}")
            print(f"{UBUNTU_WINDOWS_BASE_COMMAND} {BASE_TEST_COMMAND}")


if __name__ == '__main__':
    main()
