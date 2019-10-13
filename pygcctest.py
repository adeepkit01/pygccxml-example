from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser

generator_path, generator_name = utils.find_xml_generator()

xml_generator_config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name)

filename = "example.hpp"

decls = parser.parse([filename], xml_generator_config)
global_namespace = declarations.get_global_namespace(decls)
ns = global_namespace.namespace("ns")

func = ns.free_function(name="TestFunction")

try:
    print(func.arguments[0] < func.arguments[1])
except TypeError as TE:
    print(TE)
