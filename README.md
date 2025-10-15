# festis

A simple RESTful API for generating festanmälan .pdf's. Hook it up to your calendar and festanmäl like never before!

## Docs

You can find the documentation here: [fest.kth.it](https://fest.kth.it). There's only one endpoint which, believe it or not, generates a festanmälan .pdf from a given object.

## OpenAPI

The OpenAPI specification for this API can be found here: [fest.kth.it/openapi.json](https://fest.kth.it/openapi.json).

With that, you can easily generate client libraries for your favorite programming language.

## TODO

- [ ] Implement "business logic". (One person can't be both X and Y, the event can't start before it ends and so on.)
- [ ] Properly input the dropdown selection fields.
- [ ] Implement proper bulk input.
