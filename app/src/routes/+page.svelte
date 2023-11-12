<script>
	import Dashboard from './components/Dashboard.svelte';
</script>

<svelte:head>
	<title>Spout | Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section class="flex-1 p-4">
	<div class="self-start flex flex-col items-start gap-3">
		<h1 class="text-3xl font-mono">Dashboard</h1>
	</div>
	<Dashboard />
</section>
  

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
