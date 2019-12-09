# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['cdn'] = """
type: group
short-summary: Manage Azure Content Delivery Networks (CDNs).
"""

helps['cdn custom-domain'] = """
type: group
short-summary: Manage Azure CDN Custom Domains to provide custom host names for endpoints.
"""

helps['cdn custom-domain create'] = """
type: command
short-summary: Create a new custom domain to provide a hostname for a CDN endpoint.
long-summary: >
    Creates a new custom domain which must point to the hostname of the endpoint.
    For example, the custom domain hostname cdn.contoso.com would need to have a
    CNAME record pointing to the hostname of the endpoint related to this custom
    domain.
parameters:
  - name: --profile-name
    type: string
    short-summary: Name of the CDN profile which is unique within the resource group.
  - name: --endpoint-name
    type: string
    short-summary: Name of the endpoint under the profile which is unique globally.
  - name: --hostname
    type: string
    short-summary: The host name of the custom domain. Must be a domain name.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az cdn custom-domain create -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name --hostname www.example.com
"""

helps['cdn custom-domain delete'] = """
type: command
short-summary: Delete the custom domain of a CDN.
examples:
  - name: Delete a custom domain.
    text: >
        az cdn custom-domain delete -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name
"""

helps['cdn custom-domain show'] = """
type: command
short-summary: Show details for the custom domain of a CDN.
examples:
  - name: Get the details of a custom domain.
    text: >
        az cdn custom-domain show -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name
"""

helps['cdn edge-node'] = """
type: group
short-summary: View all available CDN edge nodes.
"""

helps['cdn endpoint'] = """
type: group
short-summary: Manage CDN endpoints.
"""

helps['cdn endpoint create'] = """
type: command
short-summary: Create a named endpoint to connect to a CDN.
examples:
  - name: Create an endpoint to service content for hostname over HTTP or HTTPS.
    text: >
        az cdn endpoint create -g group -n endpoint --profile-name profile \\
            --origin www.example.com
  - name: Create an endpoint with a custom domain origin with HTTP and HTTPS ports.
    text: >
        az cdn endpoint create -g group -n endpoint --profile-name profile \\
            --origin www.example.com 88 4444
  - name: Create an endpoint with a custom domain with compression and only HTTPS.
    text: >
        az cdn endpoint create -g group -n endpoint --profile-name profile \\
            --origin www.example.com --no-http --enable-compression
"""

helps['cdn endpoint delete'] = """
type: command
short-summary: Delete a CDN endpoint.
examples:
  - name: Delete a CDN endpoint.
    text: >
        az cdn endpoint delete -g group -n endpoint --profile-name profile-name
"""

helps['cdn endpoint list'] = """
type: command
short-summary: List available endpoints for a CDN.
examples:
  - name: List all endpoints within a given CDN profile.
    text: >
        az cdn endpoint list -g group --profile-name profile-name
"""

helps['cdn endpoint load'] = """
type: command
short-summary: Pre-load content for a CDN endpoint.
examples:
  - name: Pre-load Javascript and CSS content for an endpoint.
    text: >
        az cdn endpoint load -g group -n endpoint --profile-name profile-name --content-paths \\
            '/scripts/app.js' '/styles/main.css'
"""

helps['cdn endpoint purge'] = """
type: command
short-summary: Purge pre-loaded content for a CDN endpoint.
examples:
  - name: Purge pre-loaded Javascript and CSS content.
    text: >
        az cdn endpoint purge -g group -n endpoint --profile-name profile-name --content-paths \\
            '/scripts/app.js' '/styles/*'
"""

helps['cdn endpoint start'] = """
type: command
short-summary: Start a CDN endpoint.
examples:
  - name: Start a CDN endpoint.
    text: >
        az cdn endpoint start -g group -n endpoint --profile-name profile-name
"""

helps['cdn endpoint stop'] = """
type: command
short-summary: Stop a CDN endpoint.
examples:
  - name: Stop a CDN endpoint.
    text: >
        az cdn endpoint stop -g group -n endpoint --profile-name profile-name
"""

helps['cdn endpoint update'] = """
type: command
short-summary: Update a CDN endpoint to manage how content is delivered.
examples:
  - name: Turn off HTTP traffic for an endpoint.
    text: >
        az cdn endpoint update -g group -n endpoint --profile-name profile --no-http
  - name: Enable content compression for an endpoint.
    text: >
        az cdn endpoint update -g group -n endpoint --profile-name profile \\
            --enable-compression
"""

helps['cdn endpoint add-rule'] = """
type: command
short-summary: Add a delivery rule to a CDN endpoint.
examples:
  - name: Create a global rule to disable caching.
    text: >
        az cdn endpoint add-rule -g group -n endpoint --profile-name profile --order 0\\
            --rule-name global --action-name CacheExpiration --cache_behavior BypassCache
  - name: Create a rule for http to https redirect
    text: >
        az cdn endpoint add-rule -g group -n endpoint --profile-name profile --order 1\\
            --rule-name "redirect" --match-variable RequestScheme --operator Equal --match-values HTTPS\\
            --action-name "UrlRedirect" --redirect-protocol Https --redirect-type Moved
"""

helps['cdn endpoint add-condition'] = """
type: command
short-summary: Add a condition to a delivery rule.
examples:
  - name: Add a remote address condition.
    text: >
        az cdn endpoint add-condition -g group -n endpoint --profile-name profile --rule-name name\\
            --match-variable RemoteAddress --operator GeoMatch --match-values "TH"
"""

helps['cdn endpoint add-action'] = """
type: command
short-summary: Add an action to a delivery rule.
examples:
  - name: Add a redirect action.
    text: >
        az cdn endpoint add-action -g group -n endpoint --profile-name profile --rule-name name\\
            --action-name "UrlRedirect" --redirect-protocol HTTPS --redirect-type Moved
  - name: Add a cache expiration action
    text: >
        az cdn endpoint add-action -g group -n endpoint --profile-name profile --rule-name name\\
            --action-name "CacheExpiration" --cache_behavior BypassCache
"""

helps['cdn endpoint remove-action'] = """
type: command
short-summary: Remove an action from a delivery rule.
examples:
  - name: Remove the first action.
    text: >
        az cdn endpoint remove-action -g group -n endpoint --profile-name profile --rule-name name\\
            --index 0
"""

helps['cdn endpoint remove-condition'] = """
type: command
short-summary: Remove a condition from a delivery rule.
examples:
  - name: Remove the first condition.
    text: >
        az cdn endpoint remove-action -g group -n endpoint --profile-name profile --rule-name name\\
            --index 0
"""

helps['cdn endpoint remove-rule'] = """
type: command
short-summary: Remove a delivery rule from an endpoint.
examples:
  - name: Remove the global rule.
    text: >
        az cdn endpoint remove-action -g group -n endpoint --profile-name profile --rule-name Global\\
"""

helps['cdn origin'] = """
type: group
short-summary: List or show existing origins related to CDN endpoints.
"""

helps['cdn profile'] = """
type: group
short-summary: Manage CDN profiles to define an edge network.
"""

helps['cdn profile create'] = """
type: command
short-summary: Create a new CDN profile.
parameters:
  - name: --sku
    type: string
    short-summary: >
        The pricing tier (defines a CDN provider, feature list and rate) of the CDN profile.
        Defaults to Standard_Akamai.
examples:
  - name: Create a CDN profile using Verizon premium CDN.
    text: >
        az cdn profile create -g group -n profile --sku Premium_Verizon
  - name: Create a new CDN profile. (autogenerated)
    text: az cdn profile create --location westus2 --name profile --resource-group group --sku Standard_Verizon
    crafted: true
"""

helps['cdn profile delete'] = """
type: command
short-summary: Delete a CDN profile.
examples:
  - name: Delete a CDN profile.
    text: >
        az cdn profile delete -g group -n profile
"""

helps['cdn profile list'] = """
type: command
short-summary: List CDN profiles.
examples:
  - name: List CDN profiles in a resource group.
    text: >
        az cdn profile list -g group
"""

helps['cdn profile update'] = """
type: command
short-summary: Update a CDN profile.
examples:
  - name: Update a CDN profile. (autogenerated)
    text: az cdn profile update --name MyCDNProfileWhichIsUniqueWithinResourceGroup --resource-group MyResourceGroup
    crafted: true
"""
