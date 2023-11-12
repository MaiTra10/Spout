<script>
  export let card;
  let status = false;
  import Form from './form.svelte';
</script>

<div>
  <h1>{card.name}</h1>
  <h2>{card.seed}</h2>
  <h3>{card.period}</h3>
</div>

