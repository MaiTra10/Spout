<script>
    let name = '';
    let seedType = '';
    let period = '';
  
    function handleSubmit() {
      console.log('Name:', name);
      console.log('Seed Type:', seedType);
      console.log('Period:', period);
    }
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <label for="name">Name:</label>
    <input type="text" id="name" bind:value={name} />
  
    <label for="seedType">Seed Type:</label>
    <input type="text" id="seedType" bind:value={seedType} />
  
    <label for="period">Period:</label>
    <input type="text" id="period" bind:value={period} />
  
    <button type="submit">Submit</button>
  </form>
  