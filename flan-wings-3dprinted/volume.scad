$fn=16;

linear_extrude(height=1, center=false, convexity=10)
{
   import(file="outline.dxf", layer="1mm");
}

linear_extrude(height=2, center=false, convexity=10)
{
   import(file="outline.dxf", layer="tall");
}