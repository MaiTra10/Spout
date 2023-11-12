# Spout :house_with_garden:
Spout aims to solve the issue of homeowners and gardeners inefficiently watering their plants. It is said that up to 50% of the water used to water plants is wasted. Then how could we help inform these people with good watering habits? With remote watering activation, water tracking and weather based watering tips.

We achieve this by creating an ecosystem of apps and systems that allow the user to basically keep a remote collection of all their sprinklers on either a website built using Svelte and a desktop app built using pyqt6. There is also a backend written in Python which is a TCP socket program built from the ground into an API. The apps use HTTP requests in a CRUD format to create new sprinklers, remove existing ones, update values and retrieve all sprinklers. The API also enables the user to start and/or stop the sprinkler at any given moment which then returns an overview of when the sprinkler wa sstarted how long the sprinkler ran for, to allow you to keep track of your watering habits

<b><i>*We were unable to complete all parts of this project so we do not have a live demo, but feel feel free to check out the demos provided below</i></b>

# Demos :tv:

<details>
  <summary>Server Sprinkler Demo</summary>
  <img src="gifs and screenshots/client.gif" alt="A GIF of the server interactions" height="450">
  <img src="gifs and screenshots/server.gif" alt="A GIF of the server interactions" height="450">
</details>

<details>
  <summary>Desktop Demo</summary>
  <img src="gifs and screenshots/desktop.gif" alt="A GIF of the desktop app" height="450">
</details>

<details>
  <summary>Web App Demo</summary>
  <img src="gifs and screenshots/client.gif" alt="A GIF of the web app" height="450">
</details>
