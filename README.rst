************************
Vegetation in pyDeltaRCM
************************

This repository houses an implementation of the "DeltaRCM Vegetation" model from Lauzon and Murray (2018), built on top of `the pyDeltaRCM model <https://github.com/DeltaRCM/pyDeltaRCM>`_.

With *pyDeltaRCM* installed, simply run ``python VegetationModel.py`` for a fast-running demonstration of the model.

.. figure:: https://raw.githubusercontent.com/amoodie/Vegetation_pyDeltaRCM/main/vegetation_output/simple_movie.gif

You can modify the code at the bottom of ``VegetationModel.py`` and/or ``vegetation.yaml`` to create your own simulations.

Interested in further modifying the ``VegetationModel``? Use ``hooks`` and overwriting as needed, and we suggest adding additional behavior as new methods that are called in the existing sequence.

See:
 * `documentation for using hooks in pyDeltaRCM <https://deltarcm.org/pyDeltaRCM/guides/user_guide.html#customizing-model-operations-with-subclasses-and-hooks>`_
 * <add link to multi-behavior example in pyDeltaRCM docs>


Information
-----------

For more information about the model implementation, please see the ``VegetationModel`` docstring in ``VegetationModel.py`` (`link <https://github.com/amoodie/Vegetation_pyDeltaRCM/blob/main/VegetationModel.py>`_).

For more information on the *pyDeltaRCM* model, and how to further modify
the `VegetationModel`, please see the `project documentation <https://deltarcm.org/pyDeltaRCM/index.html>`_.


References
----------

Lauzon, R., & Murray, A. B. (2018). Comparing the cohesive effects 
    of mud and vegetation on delta evolution. Geophysical Research
    Letters, 45, 10437–10445. https://doi.org/10.1029/2018GL079405

Original source code associated with the paper is archived on Zenodo at
    `doi: 10.5281/zenodo.1434243 <https://zenodo.org/record/1434243#.W6jxeP5TnKI>`_.
