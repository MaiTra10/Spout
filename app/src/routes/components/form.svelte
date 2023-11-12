<script>
  export let card;
  export let updateCard;

  let errorMessage = '';

  function handleSubmit() {
    // Check if required fields are not empty
    if (!card.name || !card.seed || !card.period) {
      // Set an error message
      errorMessage = 'Please fill in all required fields.';
    } else {
      // Clear any previous error message
      errorMessage = '';

      // Do form submission logic
      updateCard(card);
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col  w-full shadow-md shadow-gray-300 p-8 rounded-lg">
  {#if errorMessage}
    <p style="color: red;">{errorMessage}</p>
  {/if}
  <div class="flex flex-col gap-3">
    
    <div class="flex flex-col">
      <label for="name">Name:</label>
      <input type="text" id="name" bind:value={card.name} class="border-2 border-primary rounded-md w-1/4"/>
    </div>

    <div class="flex flex-col">
      <label for="seedType">Seed Type:</label>
      <input type="text" id="seedType" bind:value={card.seed} class="border-2 border-primary rounded-md w-1/4"/>
    </div>

    <div class="flex flex-col">
      <label for="period">Duration:</label>
      <input type="number" id="period" bind:value={card.period} class="border-2 border-primary rounded-md w-1/4"/>
    </div>

  </div>
  <button type="submit" class="bg-primary h-12 w-36 rounded-md text-white self-center">Submit</button>
</form>
