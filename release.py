"""
Script to build Sass lib release and ZIP archive with correct release version

Accept either '-f' or '--force' argument to force release even if past
released version is inferior, equal or superior.
"""
import os
import io
import zipfile
import sys

from cmp_version import cmp_version, VersionString

from project import __version__


# Headers to include at beginning of main Sass lib file
HEADERS = [
    "// Sveetoy {version}\n",
    "// https://sveetch.github.io/Sveetoy/\n",
    "// Copyright 2017-2019 David Thenon.\n",
    "// MIT License\n",
]


def get_released_version(past_version_file, startpath=None):
    """
    Get past released version from ``past_version_file`` file
    """
    path = past_version_file
    if startpath:
        path = os.path.join(startpath, path)

    if not os.path.exists(path):
        return None
    else:
        with io.open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content


def bump_headers(content, new_version):
    """
    Replace previous source headers with updated ones for new version
    """
    output = []
    for line in content:
        if not line.startswith('//'):
            output.append(line)

    return (''.join(HEADERS+output)).format(version=new_version)


def make_zip(sourcedir, destination, arcdir=None):
    """
    Create ZIP archive from lib sources

    * Does not try to add empty directory, only files
    * Paths inside archive are relative to given ``sourcedir`` argument;
    * If ``arcdir`` argumen is not empty, use it to prefix every path inside
      archive;
    """
    archived = []

    # Create directory if does not exists
    dest_dir = os.path.dirname(destination)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with zipfile.ZipFile(destination, 'w') as zf:
        for dirname, subdirs, files in os.walk(sourcedir):
            for filename in files:
                # Get a relative path so we dont archive full repository path
                relpath = os.path.relpath(dirname, sourcedir)
                if relpath == '.':
                    relpath = ''

                arcname = os.path.join(arcdir or '', relpath, filename)

                zf.write(os.path.join(dirname, filename), arcname)
                archived.append(arcname)

    return archived


def build_sasslib_archive(sourcepath, new_version, past_version_file,
                          archive_path, archive_indir=None):
    """
    Update main Sass library source headers then create an archive of sources
    """
    if not os.path.exists(sourcepath):
        raise Exception(("Unable to find main Sass lib "
                         "source: {}").format(sourcepath))
    else:
        print("* Update main Sass library file: {}".format(sourcepath))
        with io.open(sourcepath, 'r', encoding='utf-8') as f:
            content = [i for i in f]

        updated_content = bump_headers(content, new_version)

        with io.open(sourcepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        sourcedir = os.path.dirname(sourcepath)
        print("* Building updated ZIP archive to: {}".format(archive_path))
        print("  - Using sources from: {}".format(sourcedir))
        make_zip(sourcedir, archive_path, arcdir=archive_indir)

        # Update RELEASED_VERSION file content
        with io.open(past_version_file, 'w', encoding='utf-8') as f:
            f.write(unicode(new_version))


    return


if __name__ == "__main__":
    PAST_VERSION_FILE = "RELEASED_VERSION"
    SASSLIB_MAIN_SOURCEPATH = "sources/sass/sveetoy/sveetoy.scss"

    current_pkg_version = VersionString(__version__)
    past_released_version = VersionString(get_released_version(PAST_VERSION_FILE))

    archive_path = "dist/Sveetoy-sass-{}.zip".format(current_pkg_version)
    archive_indir = 'Sveetoy'

    print("* Current pkg version: {}".format(current_pkg_version))
    print("* Past released version: {}".format(past_released_version))

    # If force arg is given, reset past released version counter so current
    # package version is allways valid
    if '-f' in sys.argv[1:] or '--force' in sys.argv[1:]:
        print("* Forcing release ('--force' arg used) to: {}".format(current_pkg_version))
        past_released_version = 0

    # Validate than current version is superior to past released version
    if current_pkg_version > past_released_version:
        msg = "* New version to release: {}"
        print(msg.format(current_pkg_version))
        build_sasslib_archive(SASSLIB_MAIN_SOURCEPATH, current_pkg_version,
                              PAST_VERSION_FILE,
                              archive_path, archive_indir)

    elif current_pkg_version == past_released_version:
        msg = "Current version has allready been released: {}"
        raise Exception(msg.format(current_pkg_version))

    elif current_pkg_version < past_released_version:
        msg = ("Released version '{}' is superior to the one from current "
               "package '{}'")
        raise Exception(msg.format(current_pkg_version, past_released_version))
