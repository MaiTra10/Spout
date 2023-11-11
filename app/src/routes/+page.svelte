<script>
	import Counter from './Counter.svelte';

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<div>
		<h1>Dashboard</h1>
		<button class="bg-green-600 h-12 w-36 rounded-md text-white flex justify-center items-center">Outdoor</button>
	</div>

	<Counter />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	h1 {
		width: 100%;
	}
</style>
