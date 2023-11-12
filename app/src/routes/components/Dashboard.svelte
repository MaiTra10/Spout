<script>
  import { onMount } from 'svelte';
  import Card from './Card.svelte';
  import Form from './form.svelte';
  
  let cards = [];

  function addCard() {
    let card = {
      name: null,
      seed: null,
      period: null,
      set: false
    }
    cards = [...cards, card]; // Add a new card to the array
  }

  // Execute some logic after the component is mounted
  onMount(() => {
    // You can perform any initial setup here
  });
</script>


<div class="flex flex-col justify-center items-center flex-1 w-full rounded-lg mt-6">
  {#each cards as card}
    {#if card.set == false}
      <Form />
    {:else}
      <Card />
    {/if}
  {/each}
  <button class="border-2 border-primary rounded-full w-16 h-16 text-2xl text-primary" on:click={addCard}>
    +
  </button>
</div>