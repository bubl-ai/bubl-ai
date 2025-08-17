# Let's Kick Off the Raspberry Pi Adventure!

## Why Start from Scratch?
Starting from scratch is like starting a video game on easy mode – it's the best way to learn, have some fun, and maybe break a few things along the way - because let's be real, that's where the real learning happens!

I recently got my hands on the shiny new RPi 5 and thought, "Why not turn this setup into a fun experience to share with all of you?" So here we are, diving into the setup needed to kickstart your AI projects on the RPi.

## What you will learn here:

1. Connect to your RPi using SSH
2. Install Docker
3. Install VSCode and relevant extensions
4. Connect to GitHub with SSH


## 1. Connect to your RPi using SSH

For a more detailed explanation you can use [this link](https://www.raspberrypi.com/documentation/computers/remote-access.html).

### Make Your RPi Discoverable
+ Head to RPi Configuration > Interfaces
+ Turn on the switches for ssh

## 2. Install docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker [user_name]
```
After executing this, make sure to reboot your RPi to make sure the installation is complete. You can test docker by executing the next commands.[^fn-nth-4]

```bash
docker version
docker info
docker run hello-world
```

## 3. Install VSCode and relevant extensions
```bash
sudo apt install code
```

## 4. Connect to GitHub with SSH
+ Generate new ssh key, `ssh-keygen -t ed25519 -C "[your_email@domain.com]"`
+ Start the agent in the background, `eval "$(ssh-agent -s)"`
+ Add your key to the agent, `ssh-add ~/.ssh/id_ed25519`
+ Copy your key by printing it in the terminal, `cat ~/.ssh/id_ed25519.pub`
+ Sign in to your GitHub account and go to Settings > Access > SSH and GPG > New SSH key. Paste the content of your key there.
+ Test your connection, `ssh -T git@github.com`
+ Now you can clone your repo, `git clone git@github.com:[username]/[repo_name][^fn-nth-5]


## References
[^fn-nth-4]: https://www.simplilearn.com/tutorials/docker-tutorial/raspberry-pi-docker
[^fn-nth-5]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
