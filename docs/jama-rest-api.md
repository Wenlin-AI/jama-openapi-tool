# Jama REST API Overview

The official documentation for Jama's REST API is hosted at [rest.jamasoftware.com](https://rest.jamasoftware.com/). It describes all available endpoints, parameters, response formats and authentication details. Below is a short overview of what you can find there.

## Endpoint Catalog

The site lists every REST endpoint grouped by resource type. Some of the main endpoint groups include:

- **abstractitems** – generic access to items, test plans, test cycles, test runs and attachments
- **activities** – recent activity in the system
- **attachments** – file attachments to items
- **baselines** – baseline snapshots of projects
- **categories** – item categories and components
- **comments** – threaded comments on items
- **files** – file uploads used by attachments
- **filters** – saved filters for item queries
- **items** – core CRUD operations for project items
- **itemtypes** – definitions of item types for projects
- **picklistoptions** and **picklists** – custom pick list values
- **projects** – project metadata and permissions
- **relationshiprulesets**, **relationships** and **relationshiptypes** – linking items to each other
- **releases** – versioned releases in a project
- **system** – server version and configuration info
- **tags** – labels that can be applied to items
- **testcycles**, **testruns** and **testplans** – test management resources
- **users** and **usergroups** – user accounts and groups

Each endpoint page details all supported HTTP methods (such as `GET`, `POST`, `PUT` and `DELETE`), required and optional parameters, sample requests and example responses.

## API Version and Formats

The current documentation covers REST API **v1** which ships with Jama Connect **9.12**. Requests and responses use JSON. Many operations support filtering, pagination and sorting through query parameters.

The site also explains the available authentication methods. Basic authentication is supported for non-SSO environments. Jama Cloud or self-hosted versions starting with 8.62 can also authenticate via OAuth using client credentials.

For complete details visit <https://rest.jamasoftware.com/> and browse the full list of operations.

