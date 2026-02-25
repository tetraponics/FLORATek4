EC Control
==========

The FLORATek 4 monitors the electrical conductivity (EC) of your water to determine the level of nutrients in the water. Measuring nutrient levels with EC is accurate and reliable, but does have some considerations that are important to understand.

Understanding EC Measurements
-----------------------------

The water that you use in your hydroponic system contains some amount of minerals and impurities which contribute to the EC reading. Your EC probe will detect these minerals, which may be 100ppm or less for systems using mostly reverse osmosis (RO) water or could be 400ppm or higher if using hard tap water. EC probes cannot differentiate between these minerals and the hydroponic nutrients you intend to add, so before adding nutrients we measure these minerals and subtract them from the displayed EC. We call this your **EC Base**.

EC Base Setting
---------------

When you input this reading as the EC base on the EC Setup page, the FLORATek will subtract it from the measured EC reading before displaying your EC:

  **Displayed EC = Measured EC – EC Base**

For this reason, your displayed EC may be negative if your EC base is larger than your measured EC. In this case, you should lower your EC base. With fresh water and no added nutrients, you should input an EC base that is as close as possible to your measured EC without being over.

How EC Base Affects Dosing
---------------------------

It is important to understand that the FLORATek control also uses the Displayed EC when calculating doses.

Let's say you wish to have 1000ppm of nutrients in your water, but your untreated water has a measured EC of 250ppm due to the impurities in your tap water. By inputting 250ppm as your EC base, the FLORATek control knows it needs to add 1000ppm of nutrients instead of just 750ppm.

Adjusting EC Base
-----------------

Your EC Base may change between water changes. Following a water change, you should adjust your EC base if the displayed EC is negative or is more than 20ppm.

.. note::

   Using the EC base setting is completely optional. You can leave it set at 0 and your control will simply use the raw reading from the EC probe to display EC and add nutrients to the water.

EC Units
--------

The FLORATek 4 uses the x500 scale for PPM conversions:

  **mS x 500 = PPM**

You can change between PPM and mS units in the System Setup menu under Units → EC Units.
