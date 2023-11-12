<script>
	// You can include any additional logic or data bindings here
  </script>
  
  <style>
	/* Styling for the tiles and grid container */
	.tile {
	  border: 1px solid #ddd;
	  padding: 20px;
	  text-align: center;
	  margin: 10px;
	  min-height: 100px;
	  background-color: #f9f9f9;
	  border-radius: 8px;
	  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	  transition: transform 0.3s ease-in-out;
	}
  
	.tile:hover {
	  transform: scale(1.05);
	}
  
	.grid-container {
	  display: grid;
	  grid-template-columns: repeat(2, 1fr);
	  gap: 20px;
	}
  </style>
  
  <div class="grid-container">
	<div class="tile">
	  <h2>Get Help</h2>
	</div>
	<div class="tile">
	  <h2>Troubleshoot Devices</h2>
	</div>
	<div class="tile">
	  <h2>FAQ</h2>
	</div>
	<div class="tile">
	  <h2>App Details</h2>
	</div>
  </div>
  