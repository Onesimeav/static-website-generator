from textnode import TextNode

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for node in old_nodes:
        splitted_node = node.text.split(delimiter)
        marked = node.text[0] == delimiter
        for subnode in splitted_node:
            if not subnode == "":
                if marked:
                    new_nodes.append(TextNode(subnode,text_type))
                else:
                    new_nodes.append(TextNode(subnode,node.text_type))
            marked = not marked
    return new_nodes