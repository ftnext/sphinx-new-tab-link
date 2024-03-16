import types

from sphinx.application import Sphinx
from sphinx.builders import Builder


class MixinDynamicInheritance:
    def __init__(self, mixin_class, new_class_name: str) -> None:
        self.mixin_class = mixin_class
        self.new_class_name = new_class_name

    def __call__(self, translator_class):
        return types.new_class(
            self.new_class_name, (self.mixin_class, translator_class), {}
        )


class TranslatorSetUp:
    def __init__(
        self, target_format: str, inheritance: MixinDynamicInheritance
    ) -> None:
        self.target_format = target_format
        self.inheritance = inheritance

    def is_target_format(self, builder: Builder) -> bool:
        return builder.format == self.target_format

    def __call__(self, app: Sphinx) -> None:
        if not self.is_target_format(app.builder):
            return

        builder = app.builder
        translator_class = app.registry.get_translator_class(builder)
        app.set_translator(
            builder.name, self.inheritance(translator_class), override=True
        )
