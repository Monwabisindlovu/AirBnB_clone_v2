#!/bin/bash

# Create CSS files in the current directory

# Create 3-footer.css
cat <<EOL > "3-footer.css"
/* 3-footer.css */

.footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}
EOL

# Create 3-header.css
cat <<EOL > "3-header.css"
/* 3-header.css */

.header {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}
EOL

# Create 4-common.css
cat <<EOL > "4-common.css"
/* 4-common.css */

.common {
    font-size: 18px;
    margin: 10px;
}
EOL

# Create 6-filters.css
cat <<EOL > "6-filters.css"
/* 6-filters.css */

.popover {
    max-height: 300px;
    overflow-y: auto;
}
EOL

echo "CSS files created successfully in the current directory"
