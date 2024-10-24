import mypackage.password_module as p
print(p.name)

# import sys
# sys.path.append('../package1')

import sys
import os

# Add the path to the directory containing the package
package_path = os.path.abspath("../package1")
if package_path not in sys.path:
    sys.path.append(package_path)

# Now you can import the package
import package1
