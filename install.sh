#!/usr/bin/env bash
set -e

APP_NAME="lenovo-battery-manager"
INSTALL_DIR="$HOME/.local/share/$APP_NAME"
BIN_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"

echo "🔋 Installing $APP_NAME..."

# Create necessary directories
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
mkdir -p "$DESKTOP_DIR"

# Copy files
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$SCRIPT_DIR/app.py" "$INSTALL_DIR/"
cp -r "$SCRIPT_DIR/icon.svg" "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/app.py"

# Create symlink in ~/.local/bin
ln -sf "$INSTALL_DIR/app.py" "$BIN_DIR/$APP_NAME"

# Create desktop entry
cat <<EOF > "$DESKTOP_DIR/$APP_NAME.desktop"
[Desktop Entry]
Type=Application
Name=Lenovo Battery Care
GenericName=Battery Conservation Manager
Comment=Manage Lenovo IdeaPad Conservation Mode and monitor battery
Exec=python3 $INSTALL_DIR/app.py
Icon=$INSTALL_DIR/icon.svg
Terminal=false
Categories=Settings;HardwareSettings;System;
Keywords=lenovo;battery;conservation;vantage;charge;
StartupNotify=true
StartupWMClass=lenovo-battery-manager
EOF

chmod +x "$DESKTOP_DIR/$APP_NAME.desktop"

# Update desktop database
if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database "$DESKTOP_DIR" >/dev/null 2>&1 || true
fi

echo "✅ $APP_NAME installed successfully!"
echo "🚀 You can now find 'Lenovo Battery Care' in your Start Menu or run '$APP_NAME' in terminal."
