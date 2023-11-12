<script>
  export let card;
  let status = false;
  let auto =  false;

  function toggleAuto() {
    auto = !auto;
    console.log(auto);
  }

</script>

<div class="flex flex-col  w-full shadow-md shadow-gray-300 p-8 rounded-lg">
  <div class="grid grid-cols-3 justify-items-center items-center gap-4 p-4">
    <div class="bg-gray-100 rounded-lg w-full h-full flex flex-col justify-center items-start font-mono p-8">
      <h2>Spout Connected: {card.name}</h2>
      {#if auto}
        <button class="bg-green-500 w-20 rounded-md text-white" on:click={toggleAuto}>Auto</button>
      {:else}
        <button class="bg-red-500 w-20 rounded-md text-white" on:click={toggleAuto}>Auto</button>
      {/if}
    </div>
    <div class="bg-gray-100 rounded-lg w-full h-full flex flex-col justify-center items-center font-mono">
      <h2>Schedule</h2>
      <div class="flex">
        <div class="border-green-500 border-2 rounded-2xl p-2 text-center">
          <h2>Period</h2>
          <h2>Every {card.period} hrs</h2>
        </div>
      </div>
    </div>
    <div class="font-mono bg-gray-100 rounded-lg w-full h-full p-4">
      <div class="flex gap-4">
        <h2>Status: </h2>
        {#if status}
          <div class="bg-green-500 border-2 border-green-600 rounded-full text-center w-6 h-6 font-mono">
            <h2>Active</h2>
          </div>
        {:else}
          <div class="bg-red-500 border-2 border-red-600 rounded-full text-center w-6 h-6 font-mono"></div>
        {/if}
      </div>
      <div>
        <h2>Seed Type: </h2>
        <h2>{card.seed}</h2>
      </div>
    </div>    
  </div>
  <div class="grid grid-cols-2 place-items-center p-2 font-mono gap-3 ">
    <div class=" w-full text-center bg-gray-100 rounded-lg">
      <h2>Recommended Watering Cycle</h2>
      <h2>(Base on Weather Information)</h2>
    </div>
    <div class="bg-gray-100 rounded-lg h-full w-full text-center">
      <h2>Every {card.period} hours</h2>
      <h2>Watered Yesterday</h2>
    </div>
  </div>
</div>

