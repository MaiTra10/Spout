<script>


  import { onMount } from 'svelte';
  import Card from './Card.svelte';
  import Form from './form.svelte';
  
  let cards = [];

  function addCard() {
    let card = {
      id: cards.length + 1,
      name: null,
      seed: null,
      period: null,
      set: false
    }
    cards = [...cards, card]; // Add a new card to the array

    fetch('http://192.168.1.86:12000', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(card),
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to add card to the database');
        }
        return response.json();
      })
      .then(data => {
        // If the backend successfully adds the card, update the local state
        cards = [...cards, data];
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle the error (show a message to the user, etc.)
      });

  }

  // Send a request to the backend to update the database
  
  function updateCard(cardToUpdate) {
    cards = cards.map(card => {
      if (card === cardToUpdate) {
        return { ...card, set: true };
      }
      return card;
    });
  }

  

  // Execute some logic after the component is mounted
  onMount(() => {
    fetch('http://192.168.1.86:12000')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch cards from the backend');
        }
        return response.json();
      })
      .then(data => {
        // Update the local state with the fetched cards
        cards = data;
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle the error (show a message to the user, etc.)
      });
  });
</script>


<div class="flex flex-col justify-center items-center flex-1 w-full rounded-lg mt-6 gap-2">
  {#each cards as card (card.id)}
    {#if !card.set}
      <Form {card} {updateCard} />
    {:else}
      <Card {card} />
    {/if}
  {/each}
  <button class="border-2 border-primary rounded-full w-16 h-16 text-2xl text-primary" on:click={addCard}>
    +
  </button>
</div>