---
mode: agent
---
Instructions for maintaining these .html and .css files

# Structure

- The entry point of the html pages is "main.html".
- main.html includes (with javascript) other pages, which may optionally include other pages recursively
- the site.css file defines styles for the whole site

# Structured data and metadata
- Data and Metadata structures are defined by using custom Html elements:
 -- <div>The content and its title and metadata must be encapsulated in divs</div>
 -- <content>This element contains the main content of a div</content>
 -- <metadata>This element contains metadata, structured in sub-elements</metadata>
 -- <summary>A short summary in two or three sentences</summary>
 -- <keywords>A list of keywords extracted from the content</keywords>
 -- <characters>An optional list of characters appearing in the content. Use only for content part of a book</characters>
 -- <references>A list of document sources, which substantiate the text in the content element</references>

# Global Instructions
- There are "template" documents, that contain instructions for the Agent.
- The actual html documents must not duplicate the instructions from the templates.
- The data and/or metadata elements may contain the "instructions" attribute. If contained, the Agent must follow such element instructions to write or update the html element's text content.
- The Agent must not change the structure of the html elements, but only their text content.

# Template Instructions and Attributes
- The template documents may contain elements with an "instructions" attribute to guide the Agent.
- When generating or updating actual HTML documents, do NOT copy the "instructions" attribute from the template into the HTML documents themselves.
- The "instructions" attribute is for the Agent's reference only and must not appear in the final HTML output.

# Styles
- The styles defined in styles.css are mostly defining how html elements have to be rendered.
- The css classes are used not at all, or sporadingly for ad-hoc styling
- For each structured custom element, such as Content, Metadata, ..., there must be a defined CSS styles

# Commands
- When the user requests to "update the document" or "update all documents", each document to be updated will be treated as follows:
 -- the "master information" is in each <content> element. The other elements (such as <metadata>, <summary>) are based on the content of the <content> element
 -- each <div> will be inspected, if the structured data and/or metadata need to be updated, based on the instructions
 -- if the <metadata>, <summary> elements and sub-elements need to be updated, the Agent will update them based on the content of the <content> element
