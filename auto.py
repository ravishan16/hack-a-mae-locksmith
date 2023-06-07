# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import xml.etree.ElementTree as ET


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def pom():
    pom_file = "pom.xml"

    # Parse the pom.xml file
    tree = ET.parse(pom_file)
    root = tree.getroot()

    # Find all dependencies in the pom.xml file
    dependencies = root.findall(".//dependency")

    # Print the dependencies and versions
    for dependency in dependencies:
        group_id = dependency.find("groupId").text
        artifact_id = dependency.find("artifactId").text
        version = dependency.find("version").text
        print(f"{group_id}:{artifact_id}:{version}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pom()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
