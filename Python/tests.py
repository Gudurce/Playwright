import asyncio
from wrapper import * 
import pytest

webSite1 = "https://the-internet.herokuapp.com/"
webSite2 = "https://example.com"
timeout = 2

@pytest.mark.asyncio
async def test_add_remove_elements():
    await start_browser()
    await goto(webSite1)
    await click ("Add/Remove Elements")
    await asyncio.sleep(timeout)
    await close_browser()

@pytest.mark.asyncio
async def test_example_website():
    await start_browser()        
    await goto(webSite2)
    title = await getTitle()
    assert "Example Domain" in title
    await close_browser()