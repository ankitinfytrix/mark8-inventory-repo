from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='mark8_inventory_repo',
    version='0.1.0',
    description="Inventory integrations for multiple ecommerce/qcommerce platforms",
    author='Ankit Pandey',
    author_email='ankit.pandey@infytrix.com',
    url='https://github.com/ankitinfytrix/mark8-inventory-repo.git',
    packages=find_packages(),
    install_requires=required_packages,
    include_package_data=True,
)
