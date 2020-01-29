# Install commons packages
sudo apt update
sudo apt install -y curl git wget zsh fonts-powerline

# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install spaceship theme
git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

cd
sed -i 's/robbyrussel/spaceship/g' .zshrc

# Activate sudo plugin
sed -i 's/(git)/(git sudo)/g' .zshrc

# Install commands syntax highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> .zshrc
source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh



