from tree_sitter import Language

Language.build_library(
  # Store the library in the `build` directory
  'D:\\PycharmProjects\\data_processing\\resources\\build\\my-languages.so',

  # Include one or more languages
  [
    'D:\\PycharmProjects\\data_processing\\resources\\tree-sitter-go-master'
  ]
)
