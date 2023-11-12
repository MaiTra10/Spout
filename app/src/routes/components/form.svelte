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

<form on:submit|preventDefault={handleSubmit}>
  {#if errorMessage}
    <p style="color: red;">{errorMessage}</p>
  {/if}

  <label for="name">Name:</label>
  <input type="text" id="name" bind:value={card.name} />

  <label for="seedType">Seed Type:</label>
  <input type="text" id="seedType" bind:value={card.seed} />

  <label for="period">Period:</label>
  <input type="text" id="period" bind:value={card.period} />

  <button type="submit">Submit</button>
</form>
