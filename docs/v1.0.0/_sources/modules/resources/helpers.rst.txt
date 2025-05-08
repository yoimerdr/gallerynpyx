helpers
-------

.. autoapifunction:: gallerynpyx.resources.helpers.guess

.. py:function:: guess(source: ATLTransform, allow_same: bool = True) -> AnimationResource
    :no-index:

    .. include:: _guess_doc.txt

.. py:function:: guess(source: Movie, allow_same: bool = True) -> VideoResource
    :no-index:

    .. include:: _guess_doc.txt

.. py:function:: guess(source: Image, allow_same: bool = True) -> ImageResource
    :no-index:

    .. include:: _guess_doc.txt

.. py:function:: guess(source: Displayable, allow_same: bool = True) -> DisplayableResource
    :no-index:

    .. include:: _guess_doc.txt

.. py:function:: guess(source: AnyStr, allow_same: bool = True) -> Union[ImageResource, AnimationResource, VideoResource]
    :no-index:

    .. include:: _guess_doc.txt
