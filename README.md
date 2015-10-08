Oracle ATG Commerce Reference Store
=====

Version 1.1-43p
-------------

Installs and configures Oracle ATG Commerce Reference Store

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-oracle-atg/1.1-43p/meta.yml)

Features
--------

 - Install and configure Oracle ATG Commerce Reference Store 11.1

Pre-requisites
--------------

 - AWS account
 - Centos 6 x86_64 ([AWS Marketplace](https://aws.amazon.com/marketplace/pp/B00A6KUVBW))
 - Oracle ATG 11.1 and ATG CRS 11.1 distribution [Web site](http://www.oracle.com/us/products/applications/atg/web-commerce/index.html)
 - Oracle Endeca Guided Search 11.1 distribution:
   - MDEX 6.5.1 (V46002-01.zip)
   - Platform and Services 11.1 (V45999-01.zip)
   - Tools and Frameworks 11.1 (V46387-01.zip)
   - CAS 11.1 (V46393-01.zip)
 - Pre-requisites from dependent components:
   - [Oracle Database](https://github.com/qubell-bazaar/component-oracle-db/)
   - [Oracle WebLogic](https://github.com/qubell-bazaar/component-oracle-weblogic/)

Configuration
-------------

 - Launch/configure Cloud Account in desired region:
   - N.California (us-west-1)
   - Oregon (us-west-2)
   - N.Virginia (us-east-1)
 - Create enviroment property `oracle_atg_install` with type `map<string, object>` and contents:
```
platform: "http://url.to/OCPlatform11.1.bin"
crs: "http://url.to/OCReferenceStore11.1.bin"
```
 - Create enviroment property `oracle_endeca_install` with type `map<string, object>` and contents:
```
mdex: "http://url.to/V46002-01.zip"
platform: "http://url.to/V45999-01.zip"
tools: "http://url.to/V46387-01.zip"
cas: "http://url.to/V46393-01.zip"
```
 - Create properties for dependent components: [Oracle Database](https://github.com/qubell-bazaar/component-oracle-db/), [Oracle WebLogic](https://github.com/qubell-bazaar/component-oracle-weblogic/)
