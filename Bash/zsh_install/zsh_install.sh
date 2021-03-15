#!/bin/bash

# Make an install of Zsh and oh-my-zsh

# Make sure sudo has been used
# read -p "Avez-vous utiliser sudo ? " IS_SUDO
# if [[ ${IS_SUDO} != @(y*|Y*|o*|O*) ]]
# then
#     echo "Merci d'utiliser sudo"
#     exit 1
# fi

# Make sure the script is being executed with superuser privileges.
ROOT_UID="0"
if [[ ${UID} -ne ${ROOT_UID} ]]
then
    # Install oh-my-zsh
    chmod +x install.sh
    ./install.sh

    # Download zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

    # Download zsh-completions
    git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions

    # Download zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

    # Download spaceship theme
    git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"
    ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

    # Add plugins and theme to .zshrc
    sed -i 's/(git)/(git zsh-syntax-highlighting zsh-completions zsh-autosuggestions sudo)/g' ~/.zshrc
    sed -i 's/robbyrussell/spaceship/g' ~/.zshrc

    source ~/.zshrc

    # Run zsh

    exec zsh -l
fi

# Install commons
apt update -qq
apt install -qq -y curl zsh git

# Change default shell
read -p "Enter yout username : " USER_NAME
chsh -s /bin/zsh ${USER_NAME}

# Change user 
exec su ${USER_NAME} ${0}

