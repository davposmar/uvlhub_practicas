import sys
from importlib.metadata import distributions
from packaging.specifiers import SpecifierSet
from packaging.version import Version

versions = sys.argv[1:]

print("Versions to check:")
for version in versions:
    print(version)


for dist in distributions():
    name = dist.metadata["Name"]
    req = dist.metadata.get("Requires-Python")

    if req:
        spec = SpecifierSet(req)
        spec_versions = []
        any_version_not_supported = True
        for version in versions:
            supports = Version(version) in spec
            any_version_not_supported = any_version_not_supported and supports
            spec_versions.append((version, supports))
                  
        if not any_version_not_supported:
            txt = ""
            for (_version, _support,) in spec_versions:
                txt += f"{_version}={_support} "
            print(
                f"{name}: {req} "
                f"({txt})"
            )
