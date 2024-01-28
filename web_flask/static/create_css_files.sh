 #!/bin/bash
# Create CSS files in the web_flask/static/styles directory

CSS_DIR="web_flask/static/styles"

# Create 3-footer.css
cat <<EOL > "${CSS_DIR}/3-footer.css"
/* 3-footer.css */

.footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}
EOL

# Create 3-header.css
cat <<EOL > "${CSS_DIR}/3-header.css"
/* 3-header.css */

.header {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}
EOL

# Create 4-common.css
cat <<EOL > "${CSS_DIR}/4-common.css"
/* 4-common.css */

.common {
    font-size: 18px;
    margin: 10px;
}
EOL

# Create 6-filters.css
cat <<EOL > "${CSS_DIR}/6-filters.css"
/* 6-filters.css */

.popover {
    max-height: 300px;
    overflow-y: auto;
}
EOL

echo "CSS files created successfully in ${CSS_DIR}"
