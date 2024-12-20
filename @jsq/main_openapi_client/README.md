# main-openapi-python
An internal API for inter-service communication at JSQ.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.1.1
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import main_openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import main_openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import main_openapi_client
from main_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /internal/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = main_openapi_client.Configuration(
    host = "/internal/api/v1"
)



# Enter a context with an instance of the API client
with main_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_openapi_client.AccountsApi(api_client)
    account_contact_add_request_body = main_openapi_client.AccountContactAddRequestBody() # AccountContactAddRequestBody |  (optional)

    try:
        # API for account contact to add new or existing contact to account
        api_response = api_instance.account_contact_add(account_contact_add_request_body=account_contact_add_request_body)
        print("The response of AccountsApi->account_contact_add:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->account_contact_add: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */internal/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**account_contact_add**](docs/AccountsApi.md#account_contact_add) | **PATCH** /account-contact/add | API for account contact to add new or existing contact to account
*AccountsApi* | [**account_contact_bulk_remove**](docs/AccountsApi.md#account_contact_bulk_remove) | **DELETE** /account-contact/bulk-remove | API for account contact bulk removal
*AccountsApi* | [**account_contact_bulk_update**](docs/AccountsApi.md#account_contact_bulk_update) | **PATCH** /account-contact/bulk-update | API for account contact bulk update
*AccountsApi* | [**account_contact_change_notify**](docs/AccountsApi.md#account_contact_change_notify) | **POST** /users/{user_id}/account-contact/bulk-notify | API for account contact change notification
*AccountsApi* | [**account_contact_change_notify_by_status**](docs/AccountsApi.md#account_contact_change_notify_by_status) | **POST** /users/{user_id}/account-contact/bulk-notify-by-status | API for account contact change notification by status
*ArenasApi* | [**get_allocation_types**](docs/ArenasApi.md#get_allocation_types) | **GET** /arenas/{arena_id}/allocation_types | Get a list of allocation types for the given arena
*ArenasApi* | [**get_arena**](docs/ArenasApi.md#get_arena) | **GET** /arenas/{id}/ | Get arena
*ArenasApi* | [**get_arena_net_income_types**](docs/ArenasApi.md#get_arena_net_income_types) | **GET** /arenas/{arena_id}/net_income_allocation_types | Get allocation types for a given arena by ID
*ArenasApi* | [**get_arena_payment_settings**](docs/ArenasApi.md#get_arena_payment_settings) | **GET** /arenas/{arena_id}/payment_settings | Get payment settings for a given arena
*ArenasApi* | [**get_arenas**](docs/ArenasApi.md#get_arenas) | **GET** /arenas/ | Get a list of Arenas
*ArenasApi* | [**get_arenas_manage_account_contact_settings**](docs/ArenasApi.md#get_arenas_manage_account_contact_settings) | **GET** /arenas/manage_account_contact_settings | Get manage account contact settings for a given arenas
*BankAccountApi* | [**get_bank_account**](docs/BankAccountApi.md#get_bank_account) | **GET** /bank_account/{id} | Get a bank account (BankAccountModel)
*DiligencesApi* | [**create_diligences**](docs/DiligencesApi.md#create_diligences) | **POST** /diligences | Create a diligence object and underlying KYC/watchlists
*DiligencesApi* | [**get_diligences**](docs/DiligencesApi.md#get_diligences) | **GET** /diligences | Get a list of diligences
*DistributionApi* | [**get_distribution**](docs/DistributionApi.md#get_distribution) | **GET** /distributions/{id} | Get distribution
*DistributionBatchesApi* | [**get_distribution_batch**](docs/DistributionBatchesApi.md#get_distribution_batch) | **GET** /distribution_batches/{id}/ | Get distribution batch no authorization checks
*DistributionBatchesApi* | [**get_distributions_for_distribution_batch**](docs/DistributionBatchesApi.md#get_distributions_for_distribution_batch) | **GET** /distribution_batches/{id}/distributions | Get distributions for a distribution batch not authorization checks
*DistributionBatchesApi* | [**get_unique_position_ids_for_distribution_batches**](docs/DistributionBatchesApi.md#get_unique_position_ids_for_distribution_batches) | **POST** /distribution_batches/unique_position_ids | Get unique positions ids for distribution batches
*EntitiesApi* | [**get_distribution_batch_ids_for_entity_id**](docs/EntitiesApi.md#get_distribution_batch_ids_for_entity_id) | **GET** /entities/{id}/distribution_batch_ids | Get list of distribution batch ids for an entity
*EntitiesApi* | [**get_entities_with_positions**](docs/EntitiesApi.md#get_entities_with_positions) | **GET** /arenas/{arena_id}/entities | Get a list of investment entities with their positions in an arena
*EntitiesApi* | [**get_entity**](docs/EntitiesApi.md#get_entity) | **GET** /entities/{id} | Get an entity (AccountModel)
*EntitiesApi* | [**get_entity_ids**](docs/EntitiesApi.md#get_entity_ids) | **GET** /entity-ids | Get entity ids
*EntitiesApi* | [**get_entity_position_ids**](docs/EntitiesApi.md#get_entity_position_ids) | **GET** /entities/{id}/position_ids | Get list of position ids in an investment entity.
*EntitiesApi* | [**get_entity_positions**](docs/EntitiesApi.md#get_entity_positions) | **GET** /entities/{id}/positions | Get a list of positions in an investment entity.
*FeatureFlagsApi* | [**bulk_update_arena_feature_flags**](docs/FeatureFlagsApi.md#bulk_update_arena_feature_flags) | **POST** /feature-flags/arena-feature-flags/{arena_id}/ | Bulk Update Arena Feature Flags
*FeatureFlagsApi* | [**bulk_update_developer_feature_flags**](docs/FeatureFlagsApi.md#bulk_update_developer_feature_flags) | **POST** /feature-flags/developer-feature-flags/ | Bulk Update Developer Feature Flags
*FeatureFlagsApi* | [**get_arena_feature_flag**](docs/FeatureFlagsApi.md#get_arena_feature_flag) | **GET** /feature-flags/arena-feature-flags/{arena_id}/{feature_flag_name}/ | Arena Feature Flag
*FeatureFlagsApi* | [**get_arena_feature_flags**](docs/FeatureFlagsApi.md#get_arena_feature_flags) | **GET** /feature-flags/arena-feature-flags/{arena_id}/ | Feature Flags for Arena
*FeatureFlagsApi* | [**get_developer_feature_flag**](docs/FeatureFlagsApi.md#get_developer_feature_flag) | **GET** /feature-flags/developer-feature-flags/{feature_flag_name}/ | Developer Feature Flag
*FeatureFlagsApi* | [**get_developer_feature_flags**](docs/FeatureFlagsApi.md#get_developer_feature_flags) | **GET** /feature-flags/developer-feature-flags/ | Developer Feature Flags
*FeatureFlagsApi* | [**update_arena_feature_flag**](docs/FeatureFlagsApi.md#update_arena_feature_flag) | **PATCH** /feature-flags/arena-feature-flags/{arena_id}/{feature_flag_name}/ | Update Arena Feature Flag
*FeatureFlagsApi* | [**update_developer_feature_flag**](docs/FeatureFlagsApi.md#update_developer_feature_flag) | **PATCH** /feature-flags/developer-feature-flags/{feature_flag_name}/ | Update Developer Feature Flag
*PaymentPrefsApi* | [**associate_payment_pref_with_positions**](docs/PaymentPrefsApi.md#associate_payment_pref_with_positions) | **PATCH** /users/{user_id}/associate_payment_pref/positions | Associate payment pref with positions
*PaymentPrefsApi* | [**associate_payment_pref_with_positions_of_accounts**](docs/PaymentPrefsApi.md#associate_payment_pref_with_positions_of_accounts) | **PATCH** /users/{user_id}/associate_payment_pref/accounts | Associate payment pref with positions of account
*PaymentPrefsApi* | [**associate_payment_pref_with_positions_of_source_payment_pref**](docs/PaymentPrefsApi.md#associate_payment_pref_with_positions_of_source_payment_pref) | **PATCH** /users/{user_id}/associate_payment_pref/source_payment_pref | Associate payment pref with positions of source payment pref
*PaymentPrefsApi* | [**associate_payment_pref_with_positions_without_payment_pref**](docs/PaymentPrefsApi.md#associate_payment_pref_with_positions_without_payment_pref) | **PATCH** /users/{user_id}/associate_payment_pref/no_payment_pref | Associate payment pref with positions with no payment pref
*PaymentPrefsApi* | [**get_payment_prefs**](docs/PaymentPrefsApi.md#get_payment_prefs) | **GET** /payment_prefs | Get a list of payment prefs
*PaymentPrefsApi* | [**update_payment_pref**](docs/PaymentPrefsApi.md#update_payment_pref) | **PATCH** /payment_prefs/{id} | Update payment pref
*PermissionsApi* | [**get_granular_permissions**](docs/PermissionsApi.md#get_granular_permissions) | **GET** /arenas/{arena_id}/users/{user_id}/granular_permissions | Returns a list of granular permissions given user has.
*PermissionsApi* | [**get_object_class_level_permissions**](docs/PermissionsApi.md#get_object_class_level_permissions) | **GET** /object_class_level_permission | Determines if a user has object class level authorization provided as input an objectAuthorizationClass, [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled.
*PermissionsApi* | [**get_object_level_permissions**](docs/PermissionsApi.md#get_object_level_permissions) | **GET** /object_level_permission | Determines if a user has object level authorization provided as input an objectType, [IDs], and [Permissions]. For staff users, permissions checks are only valid in an arena with ArenaFeatureFlags.advanced_permissions enabled. For portal users, only read permissions checks are allowed.
*PositionsApi* | [**get_external_position**](docs/PositionsApi.md#get_external_position) | **GET** /arenas/{arena_id}/external_positions/{external_position_id} | Gets position of a specific arena and source
*PositionsApi* | [**get_opco_positions**](docs/PositionsApi.md#get_opco_positions) | **GET** /arenas/{arena_id}/entities/{entity_id}/opco_positions | Get a list of the entity&#39;s positions in its directly-owned operating companies.
*PositionsApi* | [**get_positions**](docs/PositionsApi.md#get_positions) | **GET** /positions | Gets positions by ids with account, investor group, and investment entity ids.
*TransactionsApi* | [**get_transaction_rollup_status**](docs/TransactionsApi.md#get_transaction_rollup_status) | **GET** /transaction-rollups/{sync_id} | Retrieve a single transaction rollup status by batch ID
*TransactionsApi* | [**get_transaction_rollup_statuses**](docs/TransactionsApi.md#get_transaction_rollup_statuses) | **GET** /transaction-rollups | Retrieves the status of transaction rollups by batch IDs
*UsersApi* | [**get_accounts_edit_access**](docs/UsersApi.md#get_accounts_edit_access) | **GET** /users/{user_id}/account-contact/edit-access | Get accounts with edit access
*UsersApi* | [**get_accounts_view_access**](docs/UsersApi.md#get_accounts_view_access) | **GET** /users/{user_id}/account-contact/view-access | Get accounts with view access
*UsersApi* | [**get_user_arena_roles**](docs/UsersApi.md#get_user_arena_roles) | **GET** /users/{user_id}/arena_roles | Get roles for each arena
*UsersApi* | [**get_user_distribution_batch**](docs/UsersApi.md#get_user_distribution_batch) | **GET** /users/{user_id}/distribution_batch/{distribution_batch_id} | Get distribution batch with authorization checks
*UsersApi* | [**get_user_distribution_batch_distributions**](docs/UsersApi.md#get_user_distribution_batch_distributions) | **GET** /users/{user_id}/distribution_batch/{distribution_batch_id}/distributions | Get distribution batch distributions for a user_id with authorization checks
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Get users


## Documentation For Models

 - [AccountContactAdd](docs/AccountContactAdd.md)
 - [AccountContactAddRequestBody](docs/AccountContactAddRequestBody.md)
 - [AccountContactAddSuccessResponse](docs/AccountContactAddSuccessResponse.md)
 - [AccountContactBulkSuccessResponse](docs/AccountContactBulkSuccessResponse.md)
 - [AddContactCommunicationPrefs](docs/AddContactCommunicationPrefs.md)
 - [Address](docs/Address.md)
 - [AllocationType](docs/AllocationType.md)
 - [Arena](docs/Arena.md)
 - [ArenaManageAccountContactSettings](docs/ArenaManageAccountContactSettings.md)
 - [ArenaNetIncomeType](docs/ArenaNetIncomeType.md)
 - [ArenaPaymentSettings](docs/ArenaPaymentSettings.md)
 - [ArenaRoles](docs/ArenaRoles.md)
 - [BankAccount](docs/BankAccount.md)
 - [BankAccountAchInfo](docs/BankAccountAchInfo.md)
 - [BulkAccountContactChangeNotify](docs/BulkAccountContactChangeNotify.md)
 - [BulkAccountContactChangeNotifyByStatus](docs/BulkAccountContactChangeNotifyByStatus.md)
 - [BulkAccountContactChangeNotifyByStatusRequestPayloadsInner](docs/BulkAccountContactChangeNotifyByStatusRequestPayloadsInner.md)
 - [BulkAccountContactChangeNotifyRequestPayloadsInner](docs/BulkAccountContactChangeNotifyRequestPayloadsInner.md)
 - [BulkAccountContactRemove](docs/BulkAccountContactRemove.md)
 - [BulkAccountContactRemoveRequestBody](docs/BulkAccountContactRemoveRequestBody.md)
 - [BulkAccountContactUpdate](docs/BulkAccountContactUpdate.md)
 - [BulkAccountContactUpdateRequestBody](docs/BulkAccountContactUpdateRequestBody.md)
 - [BulkUpdateDeveloperFeatureFlags400Response](docs/BulkUpdateDeveloperFeatureFlags400Response.md)
 - [BulkUpdateFeatureFlags](docs/BulkUpdateFeatureFlags.md)
 - [BusinessInfo](docs/BusinessInfo.md)
 - [BusinessInfoAddress](docs/BusinessInfoAddress.md)
 - [BusinessInfoDocumentsInner](docs/BusinessInfoDocumentsInner.md)
 - [BusinessInfoIndividualProfilesInner](docs/BusinessInfoIndividualProfilesInner.md)
 - [BusinessInfoInstitutionProfilesInner](docs/BusinessInfoInstitutionProfilesInner.md)
 - [ContactDetails](docs/ContactDetails.md)
 - [ContactDetailsAttributes](docs/ContactDetailsAttributes.md)
 - [ContactDetailsAttributesAddressInner](docs/ContactDetailsAttributesAddressInner.md)
 - [ContactDetailsAttributesAddressInnerAddress](docs/ContactDetailsAttributesAddressInnerAddress.md)
 - [ContactDetailsAttributesAddressInnerAddressCountry](docs/ContactDetailsAttributesAddressInnerAddressCountry.md)
 - [ContactDetailsAttributesAddressInnerAddressState](docs/ContactDetailsAttributesAddressInnerAddressState.md)
 - [ContactDetailsAttributesEmail](docs/ContactDetailsAttributesEmail.md)
 - [ContactDetailsAttributesEmploymentsInner](docs/ContactDetailsAttributesEmploymentsInner.md)
 - [ContactDetailsAttributesEmploymentsInnerEmployer](docs/ContactDetailsAttributesEmploymentsInnerEmployer.md)
 - [ContactDetailsAttributesPhoneFaxInner](docs/ContactDetailsAttributesPhoneFaxInner.md)
 - [CreateDiligence](docs/CreateDiligence.md)
 - [CreateDiligenceBusinessInfo](docs/CreateDiligenceBusinessInfo.md)
 - [CreateDiligenceDiligenceCategory](docs/CreateDiligenceDiligenceCategory.md)
 - [CreateDiligenceDiligenceType](docs/CreateDiligenceDiligenceType.md)
 - [CreateDiligenceExternalObjectType](docs/CreateDiligenceExternalObjectType.md)
 - [CreateDiligenceReferenceExternalObjectType](docs/CreateDiligenceReferenceExternalObjectType.md)
 - [DetailedEntity](docs/DetailedEntity.md)
 - [Diligence](docs/Diligence.md)
 - [DiligenceCategory](docs/DiligenceCategory.md)
 - [DiligenceExternalObjectType](docs/DiligenceExternalObjectType.md)
 - [DiligenceStatus](docs/DiligenceStatus.md)
 - [DiligenceType](docs/DiligenceType.md)
 - [Distribution](docs/Distribution.md)
 - [DistributionBatch](docs/DistributionBatch.md)
 - [DistributionBatchUniquePositionIds](docs/DistributionBatchUniquePositionIds.md)
 - [DistributionBatchUniquePositionIdsRequestBody](docs/DistributionBatchUniquePositionIdsRequestBody.md)
 - [Document](docs/Document.md)
 - [Entity](docs/Entity.md)
 - [EntityDistributionBatchIds](docs/EntityDistributionBatchIds.md)
 - [EntityPositionIds](docs/EntityPositionIds.md)
 - [Error](docs/Error.md)
 - [ExternalPosition](docs/ExternalPosition.md)
 - [FeatureFlag](docs/FeatureFlag.md)
 - [GetDeveloperFeatureFlags401Response](docs/GetDeveloperFeatureFlags401Response.md)
 - [GranularPermission](docs/GranularPermission.md)
 - [IndividualProfile](docs/IndividualProfile.md)
 - [IndividualProfileAddress](docs/IndividualProfileAddress.md)
 - [InstitutionProfile](docs/InstitutionProfile.md)
 - [InstitutionProfileAddress](docs/InstitutionProfileAddress.md)
 - [MetaData](docs/MetaData.md)
 - [ObjectAuthorizedClass](docs/ObjectAuthorizedClass.md)
 - [ObjectLevelPermission](docs/ObjectLevelPermission.md)
 - [ObjectType](docs/ObjectType.md)
 - [Opco](docs/Opco.md)
 - [OpcoPosition](docs/OpcoPosition.md)
 - [PaymentPref](docs/PaymentPref.md)
 - [PaymentPrefPaymentPrefAch](docs/PaymentPrefPaymentPrefAch.md)
 - [PaymentPrefPaymentPrefAchAchDomicileAddress](docs/PaymentPrefPaymentPrefAchAchDomicileAddress.md)
 - [PaymentPrefPaymentPrefWire](docs/PaymentPrefPaymentPrefWire.md)
 - [PaymentPrefPaymentPrefWireWireBeneficiaryAddress](docs/PaymentPrefPaymentPrefWireWireBeneficiaryAddress.md)
 - [Permission](docs/Permission.md)
 - [Position](docs/Position.md)
 - [PositionAttribute](docs/PositionAttribute.md)
 - [PositionCabsInner](docs/PositionCabsInner.md)
 - [PositionContributionsInner](docs/PositionContributionsInner.md)
 - [PositionNetIncomeSumByTypeInner](docs/PositionNetIncomeSumByTypeInner.md)
 - [ResponseStatus](docs/ResponseStatus.md)
 - [ServerError](docs/ServerError.md)
 - [TransactionRollupStatus](docs/TransactionRollupStatus.md)
 - [UpdateFeatureFlag](docs/UpdateFeatureFlag.md)
 - [UpdatePaymentPrefOptions](docs/UpdatePaymentPrefOptions.md)
 - [UpdatePositionsPaymentPrefSuccessResponse](docs/UpdatePositionsPaymentPrefSuccessResponse.md)
 - [User](docs/User.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="auth-cookie"></a>
### auth-cookie

- **Type**: API key
- **API key parameter name**: a
- **Location**: 

<a id="csrf-token"></a>
### csrf-token

- **Type**: API key
- **API key parameter name**: X-CSRF-Token
- **Location**: HTTP header


## Author



