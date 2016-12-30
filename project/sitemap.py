# -*- coding: utf-8 -*-
"""
Sitemap builder
"""
import json, os

from treelib import Tree

from optimus.conf import settings


class SitemapError(Exception):
    pass


class PageSitemap(object):
    """
    Construct ressource page to build and published sitemap
    """
    def __init__(self, tree, view, with_root=False):
        self.tree = json.loads(tree.to_json(with_data=True))
        self.view = view
        self.with_root = with_root # For public sitemap

        # Public sitemap
        self.sitemap = self.get_public_sitemap(self.tree)

        # Store a flat list of every ressources to build as pages
        self.ressources = self.recursive_ressources([self.tree])

    def get_public_sitemap(self, tree):
        """
        Return a list of sitemap nodes

        If 'PageSitemap.with_root' is False, return only root children nodes,
        else return the full dict containing root node.
        """
        if not self.with_root:
            return tree['root']['children']
        return [tree]

    def recursive_ressources(self, children, pages=[]):
        """
        Return a flat ressources list from given children
        """
        for branch in children:
            for leaf_name, leaf_content in branch.items():
                datas = leaf_content['data']
                pages.append(self.view(
                    title=leaf_name,
                    template_name=datas['link'],
                    destination=datas['link'],
                    sitemap=self.sitemap,
                ))
                if datas['is_dir']:
                    pages = self.recursive_ressources(leaf_content['children'])
        return pages


def tree_from_directory_structure(scanned_path, base_path=None):
    """
    Scan given "scanned_path" path to find every HTML page file to build sitemap.

    Assume you want to use templates file names as ressource filename url.

    * Filenames and directory starting with "_" are ignored;
    * Expect an "index.html" file in each directory (except ignored ones) which
      will take the directory name;

    Return a treelib.Tree of finded pages
    """
    tree = Tree()
    tree.create_node("root", "root", data={
        'id': "root",
        'link': 'index.html',
        'is_dir': True,
    })

    if base_path is None:
        base_path = scanned_path

    for root, dirs, files in os.walk(scanned_path):
        # Current relative dir from demos dir
        relative_dir = os.path.relpath(root, base_path)

        if not relative_dir.startswith('_'):
            if relative_dir == '.':
                parent = None
                current_dir = "root"
                dir_name = "Root"
            else:
                dir_name = os.path.basename(relative_dir)
                current_dir = relative_dir
                # Resolve parent tag
                parent = "/".join(os.path.split(relative_dir)[:-1])
                if not parent:
                    parent = "root"
                # Add directory node
                tree.create_node(dir_name.replace('_', ' '), current_dir, parent=parent, data={
                    'id': current_dir,
                    'link': os.path.join(relative_dir, 'index.html'),
                    'is_dir': True,
                })

            #print "dir_name:{dir_name} | current_dir:{current_dir} | relative_dir:{relative_dir} | parent:{parent}".format(
                #dir_name=dir_name, current_dir=current_dir, relative_dir=relative_dir, parent=parent)

            # Recursive find templates in dirs
            for item in files:
                if not item.startswith('_') and item != 'index.html':
                    # Get filepath relative to root, remove leading './'
                    filepath = os.path.join(relative_dir, item)
                    if filepath.startswith('./'):
                        filepath = filepath[2:]

                    # Build unique tag identifier
                    tag = filepath
                    #print "   * file:{filename} | tag:{tag} | parent:{parent}".format(filename=item, tag=tag, parent=current_dir)

                    # Make title
                    head, tail = os.path.splitext(item)
                    title = head.replace('_', ' ')

                    # Add file node to current directory node
                    tree.create_node(title, tag, parent=current_dir, data={
                        'id': tag,
                        'link': filepath,
                        'is_dir': False,
                    })

            #print

    return tree
