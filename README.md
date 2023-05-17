![](https://raw.githubusercontent.com/GuiEpi/mtcc/master/assets/mtcc_nfo_builder.png) ![](https://raw.githubusercontent.com/GuiEpi/mtcc/master/assets/mtcc_pres.png) 
# mtcc
#### The quick and easy way to create and share your music torrents!
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)

mtcc is a user-friendly tool designed for content creators to easily upload a music torrent. The application includes an NFO builder and a presentation generator in BBCode format, all accessible through a Streamlit web page.

Simply upload the album of your choice and mtcc will generate a downloadable NFO as well as a presentation for the album that can be copied in one click, without the need to provide any additional information.

mtcc uses [MediaInfo](https://mediaarea.net/en/MediaInfo) to extract data from audio files, ensuring that 100% of the information in the NFO is reliable. [Streamlit](https://streamlit.io) makes the application easy to use and provides a smooth user experience.

![](https://raw.githubusercontent.com/GuiEpi/mtcc/master/assets/mtcc_view.gif)

- [Dependencies](#dependencies)
- [Clone the repo](#clone-the-repo)
- [Development](#development)
- [Deployment](#deployment)
- [Contribute](#contribute)
- [Improvement ideas](#improvement-ideas)
- [License](#license)

## Dependencies
[git](https://git-scm.com/downloads)
### Development
[MediaInfo](https://mediaarea.net/en/MediaInfo), [Poetry](https://python-poetry.org/docs/#installation)
### Production
[Docker](https://docs.docker.com/get-docker/)
> See [Prerequisites](#prerequisites)


## Clone the repo 
First of all you need to clone the repo
```bash
git clone https://github.com/GuiEpi/mtcc.git
```

## Development
_If you don't want to contribute, modify or test things you can go to the [deployment section](#deployment)_
### Usage

#### Install dependencies
```bash
poetry install
```

#### Run Streamlit
```bash
poetry run streamlit run mtcc/app.py
```
> Default url [http://localhost:8501](http://localhost:8501)

## Deployment
### (optional) Add infos in `config.ini` file
The .ini file allows to define default configuration values, however it is optional
```ini
[nfo]
ripper = ripper name
uploader = uploader name

[pres]
ygg_link = https://domain_name.com/profile/profile-name
ygg_tag = TAG
default_banners = play_banners_orange
```

### Prerequisites

1. [Install Docker Engine](#install-docker-engine)
2. [Check network port accessibility](#check-network-port-accessibility)
3. [(optional) Intall docker-compose](#optional-install-docker-compose)

#### Install Docker Engine

If you haven't already done so, install [Docker](https://docs.docker.com/engine/install/#server) on your server. Docker provides `.deb` and `.rpm` packages from many Linux distributions, including:
- [Debian](https://docs.docker.com/engine/install/debian/ )
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Verify that Docker Engine is installed correctly by running the `hello-world` Docker image:
```bash
sudo docker run hello-world
```
> Follow Docker's official [post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker as a non-root user, so that you don't have to preface the `docker` command with `sudo`.

#### Check network port accessibility
As you and your users are behind your corporate VPN, you need to make sure all of you can access a certain network port. Let's say port `8501`, as it is the default port used by Streamlit. Contact your IT team and request access to port `8501` for you and your users.

#### (optional) Install docker-compose
If you want to use `docker-compose` to manage your containers, you can install it by following these steps:

1. Visit the official [docker-compose](#https://docs.docker.com/compose/install/) installation guide for detailed instructions.
2. Choose the installation method that is suitable for your operating system.


### Create and start containers

#### Without docker-compose

#### Build a Docker image
The [docker build](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile` . Run the following command from the `mtcc/` directory on your server to build the image:
```bash
docker build -t mtcc .
```
The `-t` flag is used to tag the image. Here, we have tagged the image `mtcc`. If you run:
```bash
docker images
```
You should see a `mtcc` image under the REPOSITORY column. For example:
```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
mtcc         latest    70b0759a094d   About a minute ago   1.02GB
```

#### Run the Docker container
Now that you have built the image, you can run the container by executing:
```bash
docker run -p 8501:8501 mtcc
```
The `-p` flag publishes the container’s port 8501 to your server’s 8501 port.

If all went well, you should see an output similar to the following:
```
docker run -p 8501:8501 mtcc

  You can now view mtcc app in your browser.

  URL: http://0.0.0.0:8501
```
To view mtcc app, users can browse to [`http://0.0.0.0:8501`](http://0.0.0.0:8501) or [`http://localhost:8501`](http://localhost:8501)

#### With docker-compose
`docker-compose` is a powerful tool that allows you to define and manage multi-container applications. While it excels at orchestrating multiple containers, you can also use it for simplifying the build and run process of a single container. Here's how you can use docker-compose to build and run your container with a single command:
```bash
docker-compose up --build
```
The `--build` flag ensures that the images are rebuilt if there are any changes in the Dockerfiles or build context.

If all goes well, you should see the output indicating that the containers are being built and started. Once the process is complete, you should see a message similar to the following:
```
Recreating mtcc_streamlit_1 ... done
Attaching to mtcc_streamlit_1
streamlit_1  | 
streamlit_1  | Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.
streamlit_1  |
streamlit_1  | 
streamlit_1  |   You can now view your Streamlit app in your browser.
streamlit_1  |
streamlit_1  |   URL: http://0.0.0.0:8501
streamlit_1  |
```
Your mtcc app is now running inside a container.

To view your mtcc app, open a web browser and navigate to [`http://localhost:8501`](http://localhost:8501). You should be able to access and interact with mtcc.

## Contribute

#### Fork the repository 
Before you can contribute, you need to make a copy (fork) of the repository to your own GitHub account. You can do this by clicking the "Fork" button in the upper-right corner of the repository page.

#### Clone the repository
Once you have forked the repository, you can clone it to your local machine using Git. To do this, run the following command in your terminal:
```bash
git clone https://github.com/your-username/your-repository.git
```
> Replace "your-username" and "your-repository" with the appropriate values for your fork.

#### Create a branch
Before you make any changes, it's a good idea to create a new branch to work on. This helps keep your changes separate from the main branch and makes it easier to track changes. You can create a new branch using the following command:
```bash
git checkout -b my-branch
```
> Replace "my-branch" with a descriptive name for your branch.

#### Make your changes
Now you can make your changes to the code, documentation, or other files in the repository.
#### _For the future_ Test your changes
Before you submit your changes, make sure they work as intended. Run any tests included with the project and make sure they pass. If there are no tests, you may want to consider adding some.

#### Format your code
To format your code with [Black](https://black.readthedocs.io/en/stable/getting_started.html#installation), run the following command:
```
black .
```
> This will recursively format all Python files in the current directory and its subdirectories.
#### Check the formatting
After running Black, check the formatting of your code to ensure that it is correct. You can do this by running the following command:
```
black --check . 
```
> This will check the formatting of all Python files in the current directory and its subdirectories without actually changing anything.

#### Commit your changes
Once you are satisfied with your changes, you can commit them to your branch using the following command:
```bash
git add .
git commit -m "Descriptive commit message"
```
> Replace "Descriptive commit message" with a brief summary of the changes you made.

#### Push your changes
Once you have committed your changes, you can push them to your fork using the following command:
```
git push origin my-branch
```
> Replace "my-branch" with the name of your branch.

#### Open a pull request
Finally, you can open a pull request (PR) to submit your changes to the original repository. To do this, go to your fork on GitHub and click the "New pull request" button. Make sure to select the appropriate branches (your branch and the main branch) and provide a brief description of your changes.

### Add banners
If you'd like to add banners to the project, please ensure that they meet the following requirements:

- Banners must be saved in the banners folder.
- There must be **6** banners in total, named as follows:
  - `information.png`
  - `track_details.png`
  - `technical_details.png`
  - `download.png`
  - `my_torrents.png`
  - `mtcc_pres.png`
  > You can use the `mtcc_pres.png` banner from one of the four existing banners.
- Banners must be in PNG format and have a size of 360x50 pixels.
- Banners must be saved in a folder with a name in the format of `{name}_banners_{theme}`.
- Finally, add your banner in `config.py` within the `PRES_BANNERS` dictionary, like this:
```py
PRES_BANNERS = {
    "play_banners_purple": f"{PRES_BANNERS_LINK}/play_banners_purple",
    "play_banners_orange": f"{PRES_BANNERS_LINK}/play_banners_orange",
    "kk_banners_blue": f"{PRES_BANNERS_LINK}/kk_banners_blue",
    "kk_banners_orange": f"{PRES_BANNERS_LINK}/kk_banners_orange",
    # Link to the new banners folder
    "your_new_banners": f"{PRES_BANNERS_LINK}/your_new_banners",
}
```
That's it! Once you've made your changes, submit a pull request. If your banners meet our guidelines, we'll be happy to add them to the project.

## Improvement ideas
I already have many ideas for improvement, such as:
- Linking to other album streams of the same artist in the presentation
- Adding a function to add a "like" next to a track in the presentation
- Improving the UI
- Adding a help section to access the app on a custom domain name
- Adding logging to the app for better debugging
- Adding tests for better code quality
- Adding continuous integration (CI) for automated testing and deployment
- Adding more type hints for better code readability and maintainability

## License
mtcc is completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.